import reddit
import time
import random

if __name__ == '__main__':
  while True:
    postSubmission = random.choice([True, False])
    if postSubmission:
      reddit.random_submission()
    time.sleep(random.randint(10, 30))
    postReply = random.choice([True, False])
    if postReply:
      reddit.random_reply()
    time.sleep(random.randint(600, 900))
