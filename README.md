<h1>Introduction</h1>

The PredictorProjGPT prompt framework has the capability to accept performance test results as an input and provide an output that includes Key Performance Indicators (KPIs) mapped to their corresponding dataframe objects.

<b>OpenAI Documentation</b> : https://platform.openai.com/docs/libraries/python-library 

<h1>Pre-Requisites</h1>

*1. OpenAI API Key* <br>
*2. OpenAI Packages* <br>
*3. Pandas Packages* <br>
*4. Streamlit Packages* <br>

<h3>Installing Packages</h3>

*1. Install OpenAI Packages*

```
pip install openai
```

*2. Install Pandas*

```
pip install pandas
```

*3. Install Streamlit*

```
pip install streamlit
```
<h1>Output</h1>

<h3>Input Performance Test Report Prompt</h3>

```
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
```
<h3>End Result</h3>
![image](https://github.com/sayan26/PredictorProjGPT/assets/16152685/2fc5f180-ae55-4dad-8376-da43e3ab3b04)

<h1>Installation</h1>

*1. Clone the repository into your project directory* <br>

```
git clone 'enter repository url here'
```

*2. Build Image* <br>

```
docker build -t predictor-gpt-app .
```

*2. Run the container* <br>

```
docker run -it predictor-gpt-app
```




