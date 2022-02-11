REST Chess solver

To run the application:
1. Install the requirements into a virtualenv or your environment of choice
2. run in terminal: pip install -r requirements.txt
3. run in terminal: python app.py

To test the application run below commends in different terminal:
1. 'curl /api/v1/{chess-figure}/{current-field}' to check available moves 
2. 'curl /api/v1/{chess-figure}/{current-field}/{dest-field}'  to check if move from current-field to dest-field is possible