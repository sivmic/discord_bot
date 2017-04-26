#!/usr/bin/env bash

zip -r output.zip * -x "output.zip"
scp -i "/Users/air/Google Drive/Other/aws_key.pem" output.zip ubuntu@52.59.90.213:~/handles_bot.zip
ssh -i "/Users/air/Google Drive/Other/aws_key.pem" ubuntu@52.59.90.213 "sudo rm -rf ~/handles_bot; mkdir ~/handles_bot; unzip handles_bot.zip -d ~/handles_bot; sudo systemctl restart handles_bot.service;"
