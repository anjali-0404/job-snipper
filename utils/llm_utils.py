"""
Multi-Model LLM Utility
Supports Groq, Google Gemini, and other providers with automatic fallback
"""

import os
from typing import Optional, Dict, Any, List
from dotenv import load_dotenv

load_dotenv()


class MultiModelLLM:
    """
    Unified interface for multiple LLM providers with automatic fallback
    """
    
    def __init__(self):
        self.providers = []
        self._init_providers()
    
    def _init_providers(self):
        """Initialize available LLM providers in priority order"""
        
        # 1. Try Groq (fast and reliable)
        groq_key = os.getenv("GROQ_API_KEY")
        if groq_key:
            try:
                from groq import Groq
                self.providers.append({
                    "name": "groq",
                    "client": Groq(api_key=groq_key),
                    "model": os.getenv("GROQ_MODEL", "llama-3.3-70b-versatile"),
                    "type": "groq"
                })
            except Exception as e:
                print(f"Failed to initialize Groq: {e}")
        
        # 2. Try Google Gemini
        google_key = os.getenv("GOOGLE_API_KEY") or os.getenv("GEMINI_API_KEY")
        if google_key:
            try:
                import google.generativeai as genai
                genai.configure(api_key=google_key)
                self.providers.append({
                    "name": "gemini",
                    "client": genai,
                    "model": os.getenv("GENAI_MODEL", "gemini-1.5-flash"),
                    "type": "gemini"
                })
            except Exception as e:
                print(f"Failed to initialize Gemini: {e}")
        
        # 3. Try OpenAI (if key is available)
        openai_key = os.getenv("OPENAI_API_KEY")
        if openai_key:
            try:
                from openai import OpenAI
                self.providers.append({
                    "name": "openai",
                    "client": OpenAI(api_key=openai_key),
                    "model": os.getenv("OPENAI_MODEL", "gpt-3.5-turbo"),
                    "type": "openai"
                })
            except Exception as e:
                print(f"Failed to initialize OpenAI: {e}")
        
        # 4. Try Anthropic Claude (if key is available)
        anthropic_key = os.getenv("ANTHROPIC_API_KEY")
        if anthropic_key:
            try:
                from anthropic import Anthropic
                self.providers.append({
                    "name": "anthropic",
                    "client": Anthropic(api_key=anthropic_key),
                    "model": os.getenv("ANTHROPIC_MODEL", "claude-3-haiku-20240307"),
                    "type": "anthropic"
                })
            except Exception as e:
                print(f"Failed to initialize Anthropic: {e}")
    
    def generate_content(
        self, 
        prompt: str, 
        temperature: float = 0.7,
        max_tokens: int = 2048,
        preferred_provider: Optional[str] = None
    ) -> str:
        """
        Generate content using available LLM providers with automatic fallback
        
        Args:
            prompt: The prompt to send to the LLM
            temperature: Sampling temperature (0.0 to 1.0)
            max_tokens: Maximum tokens to generate
            preferred_provider: Preferred provider name (groq, gemini, openai, anthropic)
        
        Returns:
            Generated text response
        """
        if not self.providers:
            raise Exception("No LLM providers available. Please configure API keys.")
        
        # Reorder providers if preferred provider is specified
        providers_to_try = self.providers.copy()
        if preferred_provider:
            providers_to_try.sort(
                key=lambda p: 0 if p["name"] == preferred_provider else 1
            )
        
        errors = []
        for provider in providers_to_try:
            try:
                return self._generate_with_provider(
                    provider, prompt, temperature, max_tokens
                )
            except Exception as e:
                errors.append(f"{provider['name']}: {str(e)}")
                continue
        
        # All providers failed
        raise Exception(f"All LLM providers failed. Errors: {'; '.join(errors)}")
    
    def _generate_with_provider(
        self, 
        provider: Dict[str, Any], 
        prompt: str, 
        temperature: float,
        max_tokens: int
    ) -> str:
        """Generate content with a specific provider"""
        
        if provider["type"] == "groq":
            response = provider["client"].chat.completions.create(
                model=provider["model"],
                messages=[{"role": "user", "content": prompt}],
                temperature=temperature,
                max_tokens=max_tokens
            )
            return response.choices[0].message.content
        
        elif provider["type"] == "gemini":
            model = provider["client"].GenerativeModel(provider["model"])
            generation_config = provider["client"].GenerationConfig(
                temperature=temperature,
                max_output_tokens=max_tokens
            )
            response = model.generate_content(prompt, generation_config=generation_config)
            return response.text
        
        elif provider["type"] == "openai":
            response = provider["client"].chat.completions.create(
                model=provider["model"],
                messages=[{"role": "user", "content": prompt}],
                temperature=temperature,
                max_tokens=max_tokens
            )
            return response.choices[0].message.content
        
        elif provider["type"] == "anthropic":
            response = provider["client"].messages.create(
                model=provider["model"],
                max_tokens=max_tokens,
                temperature=temperature,
                messages=[{"role": "user", "content": prompt}]
            )
            return response.content[0].text
        
        else:
            raise Exception(f"Unknown provider type: {provider['type']}")
    
    def get_available_providers(self) -> List[str]:
        """Get list of available provider names"""
        return [p["name"] for p in self.providers]
    
    def is_available(self) -> bool:
        """Check if any provider is available"""
        return len(self.providers) > 0


# Global singleton instance
_llm_instance = None


def get_llm() -> MultiModelLLM:
    """Get or create the global LLM instance"""
    global _llm_instance
    if _llm_instance is None:
        _llm_instance = MultiModelLLM()
    return _llm_instance


def generate_text(
    prompt: str, 
    temperature: float = 0.7,
    max_tokens: int = 2048,
    preferred_provider: Optional[str] = None
) -> str:
    """
    Convenience function to generate text using the global LLM instance
    
    Args:
        prompt: The prompt to send to the LLM
        temperature: Sampling temperature (0.0 to 1.0)
        max_tokens: Maximum tokens to generate
        preferred_provider: Preferred provider name (groq, gemini, openai, anthropic)
    
    Returns:
        Generated text response
    """
    llm = get_llm()
    return llm.generate_content(prompt, temperature, max_tokens, preferred_provider)
