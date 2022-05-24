# humoroo

To set up:

1. Add the GoogleNews-vectors-negative300.bin file to the backend directory
2. Run pip install -r requirements.txt
3. Run npm install in the frontend directory

To run:
1. Run 'flask run' in the backend directory
2. Run 'npm start in the frontend directory
3. React app should start on your local host (5000)

Notes:
- First time generating will take some time due to model loading. After that it should be faster.
- If images aren't generating check the terminal log - likely means an input word was incorrect, the output word was too long for the comic, or the image search results were inappropriate.
