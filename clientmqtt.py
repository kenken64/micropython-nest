from mqtt import MQTTClient 

client = MQTTClient("ISSNEST", "m12.cloudmqtt.com",user="kqcqutsu", password="MP86zXZ6Zkds", port=23743)
client.connect()
client.publish(topic="youraccount/feeds/lights", msg="ON")
client.publish(topic="youraccount/feeds/lights", msg="OFF")