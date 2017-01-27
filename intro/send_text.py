from twilio.rest import TwilioRestClient

account_sid = "ACaea91b1da23bcc2d564ec1622af2b488" # Your Account SID from www.twilio.com/console
auth_token  = "0a30aa0d07fa561c33b54daa93958748"  # Your Auth Token from www.twilio.com/console

client = TwilioRestClient(account_sid, auth_token)

message = client.messages.create(
    body="My name is Ron Burgandy?",
    to="+18053413444",    # Replace with your phone number
    from_="+18058708236") # Replace with your Twilio number

print(message.sid)
