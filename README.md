# robo-advisor

![image](https://user-images.githubusercontent.com/59658326/75120102-b14cd480-5656-11ea-9b26-b74f9db0e525.png)

## Purpose:  
This program advises client on buying stocks or cryptocurrencies. By entering your personalized API key and a stock or crypto symbol, you will be able given current price information and our portfolio adivce. 

## Set Up: 
Clone (or download) this repo onto your computer and open in GitHub desktop. After downloading to a familiar place, you can navigate there from the command line <br>

    " cd /c/Users/yourname/desktop/robo-advisor" 

## Activate Your Virtual Environment & Install Requirements:

Create a virtual environment named stocks-env using the conda commands. In your command line (gitbash) type: 

    conda create stocks-env python=3.7 #change 3.7 to match the version you use

    Conda activate stocks-env

Now, you will need to install the requirements (requests & python-dotenv) from the requirements.txt file:
    
    pip install -r requirements.txt


## API Key Assistance
Type "code" in your command line to open the robo-advisor in VSC code. You will need to create a .env file to securely run the program with your own API_KEY.

Right click the left toolbar and select new file. Name your file .env

In a new tab, visit https://www.alphavantage.co/support/ obtain a free API key. In your .env file create a variable called ALPHAVANTAGE_API_KEY and set it equal to your API_Key.
   
    ALPHAVANTAGE_API_KEY = "abc123"


## Example Output

![image](https://user-images.githubusercontent.com/59658326/75120073-734fb080-5656-11ea-851a-c7644f73bd33.png)

# Happy Investing
