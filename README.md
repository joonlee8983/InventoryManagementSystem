# To activate the virtual environment
# run following command
# This should create the the .venv folder in your directory

python -m venv venv 

# Then, to activate the virtual environment, run this command
\venv\Scripts\activate

# You will see (venv) on the command line in your terminal, if it did activate
# Now install all the requirement library for python with this command
pip install -r requirement.txt

# Now go to react-app folder
cd react-app

# Install all the necessary npm packages
npm install

# To run the backend
npm run start-backend

# then run the front-end
npm start

