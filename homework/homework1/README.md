### Problem Statement
- The project seeks to predict the short-term stock price movement of Apple Inc. using historical closing prices, trading volume, and technical indicators. The purpose is to provide investors and analysts with a data-driven tool to support decision-making in a volatile market environment.

### Stakeholder & User
- Decision owner: Retail investors and financial analysts responsible for trading or investment strategies.
- Tool/operator: Data scientists or quantitative researchers developing predictive models.

### Useful Answer
- Predictive
- Metric: A numerical forecast of Apple’s next-day closing price.
- Artifact: A binary classification indicating whether the stock price will go up or down in the next trading session.

### Assumptions & Constraints
- Historical market data captures patterns that are relevant for short-term forecasting.
- Publicly available data sources are sufficient for model development.
- External events such as earnings announcements or macroeconomic shocks may not be fully accounted for in the initial model.
- Computational resources are limited to what is available for student projects.

### Known Unknowns / Risks
- Stock price movements are influenced by unpredictable news, geopotical events, and investor sentiment, which may not be reflected in historical data.
- The model may overfit to past patterns and fail to generalize under new market conditions.
- Forecast accuracy may degrade significantly during high volatility periods, such as financial crises or earnings release weeks.

### Lifecycle Mapping
- Define problem → Scoping paragraph + repo setup.
- Collect and clean data → → Historical AAPL dataset from Yahoo Finance.
- Build baseline models → Simple moving average and regression baselines.
- Test advanced models → ML/Deep learning models such as LSTM.
- Evaluate and communicate → Results summary, visualizations, stakeholder memo.
