import logging
import time
import asyncio
import grpc

import server_pb2
import server_pb2_grpc


class SubmissionClient:
  ready = True
  metricbuff = {}
  jobbuff = {}


  def add_metric(self, metric):
    if self.ready & (metric not in self.metricbuff):
      self.ready = False
      time.sleep(0.01)
      self.metricbuff[metric] = 0.0
      self.ready = True


  def add_job(self, job):
    if self.ready & (job not in self.metricbuff):
      self.ready = False
      time.sleep(0.01)
      self.jobbuff[job] = 0.0
      self.ready = True


  def log_metric(self, metric, value):
    if self.ready:
      try:
        self.ready = False
        self.metricbuff[metric] = value
        self.send_message()
        self.ready = True
      except KeyError:
        print("Add your metric with add_metric first")


  def log_job(self, job, process):
    if self.ready:
      try:
        self.ready = False
        time.sleep(0.01)
        self.jobbuff[job] = process
        self.send_message()
        self.ready = True
      except KeyError:
        print("Add your job with log_job() first")


  async def send_message(self):
    async with grpc.aio.insecure_channel("localhost:50051") as channel:
        stub = server_pb2_grpc.ListenerStub(channel)
        logging.info('starting to send message')

        if self.ready:
            self.ready = False
            try:
                async def message_iterator():
                    for k, v in self.metricbuff.items():
                        message = server_pb2.MessageData(
                            command=0,
                            name=k,
                            value=float(v)  # Ensure value is float
                        )
                        logging.info(f'Sending Message: {k} = {v}')
                        yield message
                        await asyncio.sleep(0.01)  # Add small delay between messages

                response = await stub.ListenStream(message_iterator())
                logging.info(f"Response received: {response.ret}")
            except Exception as e:
                logging.error(f"Error during streaming: {e}")
            finally:
                self.ready = True
