# Resources for apa_cases_storage

Note: To execute apa_cases_storage, you should setup
1. n8n credentials (ProAgent uses n8n to execute its workflow.)
2. All input that is referenced in the queries inside apa_cases_storage.

## n8n credentials
1. Gmail OAuth2 API
2. Google Sheets OAuth2 API
3. Google Drive OAuth2 API
4. Postgres
   1. Host: localhost
   2. Database: postgres
   3. User: your account setting in Postgres
   4. Password: your password setting in Postgres
   5. Port: 5432 (follow setting in Postgres)
5. Header Auth (NewsAPI.org)
   1. Name: X-API-Key
6. OpenWeatherMap API
7. OpenAi
8. Slack API

## Resources
1. Google Sheets
   1. Make sure you have access to
       1. https://docs.google.com/spreadsheets/d/1JiMU318fRZguk7LmfvpeDKg72vv34bfeSjTdwl0Sj7c/edit?usp=sharing
       2. https://docs.google.com/spreadsheets/d/1yMInqpKdzm-ZC9bT0dH-HMIm4P3eAZ17K8Yn251MsJY/edit?usp=sharing
3. Google Drive
    1. Make sure your own Google Drive has this folder / file architecture
        1. ProAgentWorkspace
            1. newsapi_data/
            2. 00005_code.txt
            3. 00006_code.py
            4. abc-news_chunked_1day_articles_2025-11-11_1.csv

4. Postgres
   1. Create a server named **postgres**
   2. In this server, create a table named **bloomberg_articles**:

      ```sql
      CREATE TABLE bloomberg_articles (
          id BIGINT PRIMARY KEY,
          title TEXT,
          description TEXT,
          content TEXT,
          url TEXT,
          published_at TIMESTAMP,
          source_name TEXT,
          source_id TEXT,
          author TEXT,
          url_to_image TEXT,
          content_length INTEGER,
          export_date TIMESTAMP
      );
      ```

      ```sql
      COPY bloomberg_articles(
          id,
          title,
          description,
          content,
          url,
          published_at,
          source_name,
          source_id,
          author,
          url_to_image,
          content_length,
          export_date
      )
      FROM '/YOUR-abc-news_chunked_1day_articles_2025-11-11_1.csv'
      DELIMITER ','
      CSV HEADER;
      ```

5. Slack
    1. Make sure
        1. you have created a app named ProAgentBot
        2. you have these channels in ProAgentWorkspace
            1. general, general-test, jokes, news, weathers
            2. ProAgentBot is already in above mentioned channels(/invite @ProAgentBot in your channels)

