#!/usr/bin/env python3
"""
Test Script for Gemini Model Evaluation
Tests the Gemini model's responses to various prompts
"""

import os
import sys
import google.generativeai as genai

# Configure Gemini API
genai.configure(api_key="")

# Initialize the Gemini model
model = genai.GenerativeModel('gemini-2.0-flash')

def test_model_response(prompt):
    """Test the model's response to a given prompt"""
    try:
        response = model.generate_content(prompt)
        return response.text
    except Exception as e:
        return f"Error: {str(e)}"


def run_tests():
    """Run a series of test cases"""
    print("� Gemini Model Test Suite")
    print("=" * 50)

    test_cases = [
        ("What is artificial intelligence?", "Knowledge - Technical"),
        ("Write a poem about nature.", "Creativity"),
        ("Is the sky blue? Why?", "Scientific Explanation"),
        ("Explain quantum computing to a 5 year old.", "Simplification"),
        ("What are some safety considerations in AI development?", "Safety/Ethics")
    ]

    for prompt, category in test_cases:
        print(f"\n📝 Testing {category}")
        print(f"Prompt: {prompt}")
        print("-" * 50)
        response = test_model_response(prompt)
        print(f"Response:\n{response}")
        print("-" * 50)


def main():
    try:
        run_tests()
        print("\n✅ Test Suite Complete!")
    except Exception as e:
        print(f"\n❌ Test Suite Failed: {e}")

    print("\n🎉 Test Suite Complete!")
    print("=" * 60)


if __name__ == "__main__":
    main()