"""
Test script for Multi-Model LLM System
Run this to verify your API keys are configured correctly
"""

import sys
import os

# Add parent directory to path
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from utils.llm_utils import get_llm, generate_text

def test_multi_model():
    """Test the multi-model LLM system"""
    
    print("=" * 60)
    print("Multi-Model LLM System Test")
    print("=" * 60)
    
    # Get LLM instance
    llm = get_llm()
    
    # Check available providers
    providers = llm.get_available_providers()
    
    if not providers:
        print("\n❌ ERROR: No LLM providers configured!")
        print("\nPlease add at least one API key to your .env file:")
        print("  - GROQ_API_KEY=your_key_here")
        print("  - GOOGLE_API_KEY=your_key_here")
        print("  - OPENAI_API_KEY=your_key_here")
        print("  - ANTHROPIC_API_KEY=your_key_here")
        return False
    
    print(f"\n✅ Found {len(providers)} provider(s): {', '.join(providers)}")
    
    # Test prompt
    test_prompt = "Write a one-sentence introduction for a software engineer's cover letter."
    
    print("\n" + "-" * 60)
    print("Testing text generation...")
    print("-" * 60)
    
    try:
        response = generate_text(test_prompt, temperature=0.7, max_tokens=100)
        print(f"\n✅ SUCCESS! Generated response:")
        print(f"\n{response}\n")
        print("-" * 60)
        return True
    except Exception as e:
        print(f"\n❌ ERROR: {e}")
        print("\nPlease check:")
        print("  1. Your API keys are valid")
        print("  2. You have quota/credits remaining")
        print("  3. Your internet connection")
        return False

if __name__ == "__main__":
    success = test_multi_model()
    sys.exit(0 if success else 1)
