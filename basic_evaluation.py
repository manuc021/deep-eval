# -*- coding: utf-8 -*-
from deepeval.models import GeminiModel
from deepeval.test_case import LLMTestCase
from deepeval import assert_test
from deepeval.metrics import AnswerRelevancyMetric

def main():
    # Initialize the Gemini model
    eval_model = GeminiModel(
        model="gemini-pro",
        api_key=""
    )

    # Create test case
    test_case = LLMTestCase(
        input="How many articles are there in the Selenium webdriver python course?",
        actual_output="there are 23 articles in the course",
        context=[
            "Complete Understanding on Selenium Python API Methods with real time Scenarios on LIVE Websites\n"
            "\"Last but not least\" you can clear any Interview and can Lead Entire Selenium Python Projects from "
            "Design Stage\nThis course includes:\n17.5 hours on-demand video\nAssignments\n23 articles\n9 "
            "downloadable resources\nAccess on mobile and TV\nCertificate of completion\nRequirements",
            "What you'll learn\n*****By the end of this course,You will be Mastered on Selenium Webdriver with "
            "strong Core JAVA basics\n****You will gain the ability to design PAGEOBJECT, DATADRIVEN&HYBRID "
            "Automation FRAMEWORKS from scratch\n*** InDepth understanding of real time Selenium CHALLENGES with "
            "100 + examples\n*Complete knowledge on TestNG, MAVEN,ANT, JENKINS,LOG4J, CUCUMBER, HTML REPORTS,EXCEL "
            "API, GRID PARALLEL TESTING"
        ]
    )

    # Create metrics
    relevancy_metric = AnswerRelevancyMetric(
        model=eval_model,
        strict_mode=True,
    )

    # Run evaluation
    print("\n=== Running Evaluation ===")
    assert_test(test_case, [relevancy_metric])
    
    # Get detailed score
    score = relevancy_metric.measure(test_case)
    print(f"\nFinal Score: {score:.2f}")

if __name__ == "__main__":
    main()
