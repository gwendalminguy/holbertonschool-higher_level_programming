# HyperText Transfer Protocol

This document is a brief introduction to the HyperText Transfer Protocol.

## Difference HTTP/HTTPS

HTTP is a protocol used to transfer data over a network. It includes websites' content and all API calls made between the client and the server. HTTPS is the basically the same as HTTP, but in a secure way, using the [TLS/SSL](https://en.wikipedia.org/wiki/Transport_Layer_Security) protocol. This protocol ensures that the server is authenticated, and all data exchanges are encrypted.

## HTTP Request & Response Structure

### Request:

Request messages are sent by a client to a target server, and are structured in different parts in a specific order:

1. A request line, composed of the request method, the requested URI and the protocol version, separated by spaces.
2. Zero or more request header fields, each composed of the field name, a colon, an optional whitespace, the field value, and an optional trailing whitespace.
3. An empty line.
4. An optional message body.

Request Example:

```
GET /hello.txt HTTP/1.1
Host: www.example.com
Accept-Language: en
```

### Response:

Response messages are sent by a server to a client as a reply to its former request message, and are structured in different parts in a specific order:

1. A status line, composed of the protocol version, the status code, and an optional reason phrase, separated by spaces.
2. Zero or more response header fields, each composed of the field name, a colon, an optional whitespace, the field value, and an optional trailing whitespace
3. An empty line.
4. An optional message body.

Response Example:

```
HTTP/1.1 200 OK
Server: Apache
Content-Length: 12
Content-Type: text/plain

Hello World!
```

## HTTP Methods & Status Codes

### Request Methods:

Every HTTP request uses a [method](https://en.wikipedia.org/wiki/HTTP#Request_methods) to indicate the desired action to be performed on the identified ressource. They are case-sensitive. Most common methods are the following:

- **GET**: requests that the target resource transfer a representation of its state
- **HEAD**: requests that the target resource transfer a representation of its state, without the reprensentation data enclosed in the response body
- **POST**: requests that the target resource accept the data enclosed in the request to store it
- **PUT**: requests that the target resource create or update its state with the state defined by the data enclosed in the request
- **DELETE**: requests that the target resource delete its state

### Response Status Codes:

Every HTTP response contains a [status code](https://en.wikipedia.org/wiki/List_of_HTTP_status_codes), each having a different meaning. They are composed of three digits, and can be grouped according to the first digit. Most common status codes are the following:

- #### 1XX - Informational

	- **100 Continue**: the server has received the request headers and the client should proceed to send the request body
	- **101 Switching Protocols**: the client has requested to switch protocols and the server has accepted

- #### 2XX - Successful

	- **200 OK**: the standard response for a succesful request
	- **201 Created**: the request has been fulfilled, resulting in the creation of a new resource
	- **202 Accepted**: the request has been accepted for processing, but the processing has not been completed
	- **204 No Content**: the server successfully processed the request, and is not returning any content

- #### 3XX - Redirection

	- **300 Multiple Choice**: the requested ressource has multiple options from which the client may choose
	- **301 Moved Permanently**: the requested ressource has been permanently moved to another URI

- #### 4XX - Client Error

	- **400 Bad Request**: the request is invalid
	- **401 Unauthorized**: the request is valid and understood but the client is unauthenticated
	- **403 Forbidden**: the request is valid and understood but refused by the server
	- **404 Not Found**: the requested ressource could not be found
	- **408 Request Timeout**: the server timed out waiting for the client request

- #### 5XX - Server Error

	- **500 Internal Server Error**: the server encountered an unexpected condition
	- **501 Not Implemented**: the does not recognize the request method or is not able to fulfil the request yet
	- **502 Bad Gateway**: the server was acting as a gateway or proxy and received an invalid response from the upstream server
	- **503 Service Unavailable**: the server cannot handle the request (overloaded or maintenance)
	- **504 Gateway Timeout**: the server was acting as a gateway or proxy and did not receive a timely response from the upstream server
