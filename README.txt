# Salty Bout Observer Redux!

After much consideration I have decided to completley remake SBO from scratch. This is mainly
because i have learned a lot in the past few days and believe I can improve just about everything.

Most notably, I have removed logging entirely as it was about half the codebase and was a classic
 example of bringing a sledgehammer to crack a nut.

 I also got rid of pycharm and have been using this to experiemnt with VisualStudio Code.

# Config
in app.mnt is a file named config.txt it should look like the following:
{"l_addr": "0.0.0.0", "l_port": "50100", "sdc_addr": "SDC_ADDR", "sdc_port": "SDC_PORT", "salty_url": "https://www.saltybet.com/state.json"}

In its place is a file named "c.txt" this is so git will add /app/mnt. Ill do my best to make
 sure the real config wont be added to the github repo like lasttime.

# Docker
 # Docker commands:
 sudo docker build -t sbo:latest .
 sudo docker run --name sbo01 -p 50100:50100 --mount source=sbo_data,target=/SBO/app/mnt sbo