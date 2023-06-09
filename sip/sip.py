# Формируем пакет SIP INVITE
message_INVITE = "INVITE sip:alice@example.com SIP/2.0\r\n" \
          "Via: SIP/2.0/UDP 192.168.0.10:5061\r\n" \
          "From: <sip:bob@example.com>\r\n" \
          "To: <sip:alice@example.com>\r\n" \
          "Call-ID: 1234567890@192.168.0.10\r\n" \
          "CSeq: 1 INVITE\r\n" \
          "Contact: <sip:bob@example.com>\r\n" \
          "Content-Type: application/sdp\r\n" \
          "Content-Length: 0\r\n\r\n"
          
# Формируем пакет SIP REGISTER
message_REGISTER = "REGISTER sip:example.com SIP/2.0\r\n" \
          "Via: SIP/2.0/UDP 192.168.0.10:5061\r\n" \
          "From: <sip:bob@example.com>\r\n" \
          "To: <sip:bob@example.com>\r\n" \
          "Call-ID: 1234567890@192.168.0.10\r\n" \
          "CSeq: 1 REGISTER\r\n" \
          "Contact: <sip:bob@192.168.0.10:5061>\r\n" \
          "Content-Length: 0\r\n\r\n"
          
# Формируем пакет SIP ACK
message_ACK = "ACK sip:alice@example.com SIP/2.0\r\n" \
          "Via: SIP/2.0/UDP 192.168.0.10:5061\r\n" \
          "From: <sip:bob@example.com>;tag=12345\r\n" \
          "To: <sip:alice@example.com>;tag=54321\r\n" \
          "Call-ID: 1234567890@192.168.0.10\r\n" \
          "CSeq: 1 ACK\r\n" \
          "Content-Length: 0\r\n\r\n"
          
# Формируем пакет SIP BYE
message_BYE = "BYE sip:alice@example.com SIP/2.0\r\n" \
          "Via: SIP/2.0/UDP 192.168.0.10:5061\r\n" \
          "From: <sip:bob@example.com>;tag=12345\r\n" \
          "To: <sip:alice@example.com>;tag=54321\r\n" \
          "Call-ID: 1234567890@192.168.0.10\r\n" \
          "CSeq: 2 BYE\r\n" \
          "Content-Length: 0\r\n\r\n"
          
# Формируем пакет SIP CANCEL
message_CANCEL = "CANCEL sip:alice@example.com SIP/2.0\r\n" \
          "Via: SIP/2.0/UDP 192.168.0.10:5061\r\n" \
          "From: <sip:bob@example.com>;tag=12345\r\n" \
          "To: <sip:alice@example.com>;tag=54321\r\n" \
          "Call-ID: 1234567890@192.168.0.10\r\n" \
          "CSeq: 2 CANCEL\r\n" \
          "Content-Length: 0\r\n\r\n"

# Формируем пакет SIP UPDATE
message_UPDATE = "UPDATE sip:alice@example.com SIP/2.0\r\n" \
                 "Via: SIP/2.0/UDP 192.168.0.10:5061\r\n" \
                 "From: <sip:bob@example.com>;tag=12345\r\n" \
                 "To: <sip:alice@example.com>;tag=54321\r\n" \
                 "Call-ID: 1234567890@192.168.0.10\r\n" \
                 "CSeq: 3 UPDATE\r\n" \
                 "Content-Type: application/sdp\r\n" \
                 "Content-Length: 123\r\n" \
                 "\r\n" \
                 "v=0\r\n" \
                 "o=- 123456 654321 IN IP4 192.168.0.10\r\n" \
                 "s=Session SDP\r\n" \
                 "c=IN IP4 192.168.0.10\r\n" \
                 "t=0 0\r\n" \
                 "m=audio 1234 RTP/AVP 0 8\r\n" \
                 "a=rtpmap:0 PCMU/8000\r\n" \
                 "a=rtpmap:8 PCMA/8000\r\n"
                 
# Формируем пакет SIP REFER
message_REFER = "REFER sip:carol@example.com SIP/2.0\r\n" \
                "Via: SIP/2.0/UDP 192.168.0.10:5061\r\n" \
                "From: <sip:bob@example.com>;tag=12345\r\n" \
                "To: <sip:alice@example.com>;tag=54321\r\n" \
                "Call-ID: 1234567890@192.168.0.10\r\n" \
                "CSeq: 4 REFER\r\n" \
                "Refer-To: <sip:carol@example.com>\r\n" \
                "Referred-By: <sip:bob@example.com>\r\n" \
                "Content-Length: 0\r\n" \
                "\r\n"    
                
# Формируем пакет SIP PRACK
message_PRACK = "PRACK sip:alice@example.com SIP/2.0\r\n" \
                "Via: SIP/2.0/UDP 192.168.0.10:5061\r\n" \
                "From: <sip:bob@example.com>;tag=12345\r\n" \
                "To: <sip:alice@example.com>;tag=54321\r\n" \
                "Call-ID: 1234567890@192.168.0.10\r\n" \
                "CSeq: 2 PRACK\r\n" \
                "Content-Length: 0\r\n\r\n"  
                
# Формируем пакет SIP SUBSCRIBE
message_SUBSCRIBE = "SUBSCRIBE sip:alice@example.com SIP/2.0\r\n" \
                    "Via: SIP/2.0/UDP 192.168.0.10:5061\r\n" \
                    "From: <sip:bob@example.com>;tag=12345\r\n" \
                    "To: <sip:alice@example.com>\r\n" \
                    "Call-ID: 1234567890@192.168.0.10\r\n" \
                    "CSeq: 1 SUBSCRIBE\r\n" \
                    "Contact: <sip:bob@example.com>\r\n" \
                    "Event: presence\r\n" \
                    "Expires: 3600\r\n\r\n"

# Формируем пакет SIP NOTIFY
message_NOTIFY = "NOTIFY sip:bob@example.com SIP/2.0\r\n" \
                 "Via: SIP/2.0/UDP 192.168.0.14:5060\r\n" \
                 "From: <sip:alice@example.com>;tag=12345\r\n" \
                 "To: <sip:bob@example.com>\r\n" \
                 "Call-ID: 1234567890@192.168.0.14\r\n" \
                 "CSeq: 2 NOTIFY\r\n" \
                 "Contact: <sip:alice@example.com>\r\n" \
                 "Event: presence\r\n" \
                 "Subscription-State: active\r\n" \
                 "Content-Type: application/pidf+xml\r\n" \
                 "Content-Length: 235\r\n\r\n" \
                 "<?xml version='1.0' encoding='UTF-8'?>" \
                 "<presence xmlns='urn:ietf:params:xml:ns:pidf'" \
                 " entity='sip:alice@example.com'>" \
                 "<tuple id='s0'>" \
                 "<status>" \
                 "<basic>open</basic>" \
                 "</status>" \
                 "<contact>sip:alice@example.com</contact>" \
                 "</tuple></presence>"
                 
# Формируем пакет SIP PUBLISH
message_PUBLISH = "PUBLISH sip:alice@example.com SIP/2.0\r\n" \
                  "Via: SIP/2.0/UDP 192.168.0.10:5061\r\n" \
                  "From: <sip:bob@example.com>;tag=12345\r\n" \
                  "To: <sip:alice@example.com>\r\n" \
                  "Call-ID: 1234567890@192.168.0.10\r\n" \
                  "CSeq: 1 PUBLISH\r\n" \
                  "Contact: <sip:bob@example.com>\r\n" \
                  "Event: presence\r\n" \
                  "Content-Type: application/pidf+xml\r\n" \
                  "Content-Length: 235\r\n\r\n" \
                  "<?xml version='1.0' encoding='UTF-8'?>" \
                  "<presence xmlns='urn:ietf:params:xml:ns:pidf'" \
                  " entity='sip:bob@example.com'>" \
                  "<tuple id='s0'>" \
                  "<status>" \
                  "<basic>open</basic>" \
                  "</status>" \
                  "<contact>sip:bob@example.com</contact>" \
                  "</tuple></presence>"
                  
# Формируем пакет SIP MESSAGE
message_MESSAGE = "MESSAGE sip:alice@example.com SIP/2.0\r\n" \
                  "Via: SIP/2.0/UDP 192.168.0.10:5061\r\n" \
                  "From: <sip:bob@example.com>;tag=12345\r\n" \
                  "To: <sip:alice@example.com>\r\n" \
                  "Call-ID: 1234567890@192.168.0.10\r\n" \
                  "CSeq: 1 MESSAGE\r\n" \
                  "Contact: <sip:bob@example.com>\r\n" \
                  "Content-Type: text/plain\r\n" \
                  "Content-Length: 15\r\n\r\n" \
                  "Hello, Alice!"

# Формируем пакет SIP INFO
message_INFO = "INFO sip:alice@example.com SIP/2.0\r\n" \
               "Via: SIP/2.0/UDP 192.168.0.10:5061\r\n" \
               "From: <sip:bob@example.com>;tag=12345\r\n" \
               "To: <sip:alice@example.com>\r\n" \
               "Call-ID: 1234567890@192.168.0.10\r\n" \
               "CSeq: 1 INFO\r\n" \
               "Contact: <sip:bob@example.com>\r\n\r\n"

# Формируем пакет SIP OPTIONS
message_OPTIONS = "OPTIONS sip:alice@example.com SIP/2.0\r\n" \
                  "Via: SIP/2.0/UDP 192.168.0.10:5061\r\n" \
                  "From: <sip:bob@example.com>;tag=12345\r\n" \
                  "To: <sip:alice@example.com>\r\n" \
                  "Call-ID: 1234567890@192.168.0.10\r\n" \
                  "CSeq: 1 OPTIONS\r\n" \
                  "Contact: <sip:bob@example.com>\r\n" \
                  "Max-Forwards: 70\r\n\r\n"
