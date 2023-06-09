import struct
import time



message_NOhgfdsTIFY = "NOThgfrdessdfghIFY sip:bob@example.com SIP/2.0\r\n" \
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

message_NOTIkjhgfjhgFY = "NOTjhgfdjhgfIFY sip:bob@example.com SIP/2.0\r\n" \
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