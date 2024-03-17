from openai import OpenAI
import os
import json
import pandas as pd

client = OpenAI(
    # This is the default and can be omitted
    api_key=os.environ.get("OPENAI_API_KEY"),
)


def extract_performance_data(report_text):
    prompt = get_performance_data() + report_text
    response = client.chat.completions.create(
        model="gpt-4-0613",
        messages=[{"role": "user", "content": prompt}]
    )
    content = response.choices[0].message.content

    try:
        data = json.loads(content)
        return pd.DataFrame(data.items(), columns=["Measure", "Value"])

    except (json.JSONDecodeError, IndexError):
        pass

    return pd.DataFrame({
        "Measure": ["response time", "wait time", "Pacing", "CPU Utilization", "Memory Consumption", "Error %"],
        "Value": ["", "", "", "", "", ""]
    })


def get_performance_data():
    return '''Please retrieve response time, wait time, Pacing, CPU Utilization, Memory Consumption, Error %
    from the following performance report. If you don't get relevant information, return "". Don't make things up.
    Then retrieve the type of performance test from your intelligence. Also, predict an outcome of it in one word. 
    Always return your response as valid JSON string.
    The format of that string should be this,
    {
       "Response Time" : "5 Seconds",
       "Wait Time" : "3 Seconds",
       "Pacing" : "300 Seconds",
       "CPU Utilization" : "75%",
       "Memory Consumption" : "55%",
       "Error % " : "20%"
       "Performance Test Type" : "Load Test"
       "Outcome" : "<Insert your prediction from general sample>"
    }
    
    Performance Report
    =========================
    
    '''


if __name__ == '__main__':
    report = '''
    A performance test was conducted on 24th April 2020 on a Salesforce application. The following observation was 
    recorded by a performance tester after conclusion of the test.
    Configuration:
    1. There are total 40 transactions involved. The wait time between each transaction is 5 seconds.
    2. Total Pacing Time is configured as 180 seconds.
    
    Summary:
    1. Average Response Time for the entire duration of the test was 6.5 seconds.
    2. CPU Utilization peaked 75% in the first hour of the steady state.
    3. Memory Consumption of 88% was observed at the last hour of the steady state.
    4. Entire duration of the test was 5 hours. Endurance Test was performed.
    5. Observed 10% error on the entire duration of the test
    6. Predict the outcome
    '''

    df = extract_performance_data(report)
    print(df.to_string())
