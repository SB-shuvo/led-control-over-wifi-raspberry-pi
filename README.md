# led-control-over-wifi-raspberry-pi

I have been trying to control an LED over WiFi using Raspberry Pi 4B. ChatGPT and Gemini both could not write the required Python code. Both of them were giving "GPIO not allocated error." Then I came across Claude and it succeeded without any error. 

Here is a screenshot of the website:
![image](https://github.com/user-attachments/assets/290595f5-cac4-4157-b475-314d268e4b38)


## Instructions to set up and run the application (Copied from claude.ai):

Install the required packages on your Raspberry Pi:

    sudo apt-get update
    sudo apt-get install python3-flask python3-rpi.gpio

Create your project directory:
```
mkdir led_control_app
cd led_control_app
```

Create the application file:
```
nano app.py
```

Then paste the Python code from the first code block.

Create the templates directory and HTML file:
```
mkdir templates
nano templates/index.html
```

Then paste the HTML code from the second code block.

Run the application:
```
python3 app.py
```
Access the web interface by opening a browser on any device on your local network and navigating to:
Copyhttp://[your-raspberry-pi-ip-address]:5000


The interface has two buttons (Turn ON and Turn OFF) that control the LED, and it displays the current status of the LED. The status also updates automatically every 5 seconds.
