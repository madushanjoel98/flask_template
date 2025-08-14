key = "secret"
# HTTP Request Methods
GET = "GET"  # Requests data from a specified resource
POST = "POST"  # Submits data to be processed to a specified resource
PUT = "PUT"  # Updates a current resource with new data
PATCH = "PATCH"  # Partially updates an existing resource
DELETE = "DELETE"  # Deletes the specified resource
HEAD = "HEAD"  # Same as GET but does not return the body, only headers
OPTIONS = "OPTIONS"  # Describes the communication options for the target resource
CONNECT = "CONNECT"  # Establishes a tunnel to the server identified by the target resource
TRACE = "TRACE"  # Performs a message loop-back test along the path to the target resource

# Informational Responses (100–199)
CONTINUE = 100  # Request received, continuing process
SWITCHING_PROTOCOLS = 101  # Switching to new protocol; obey Upgrade header
PROCESSING = 102  # WebDAV: Processing will continue

# Successful Responses (200–299)
OK = 200  # Standard response for successful HTTP requests
CREATED = 201  # Request has been fulfilled, resulting in the creation of a new resource
ACCEPTED = 202  # Request has been accepted for processing, but not yet completed
NON_AUTHORITATIVE_INFORMATION = 203  # Information from a local or third-party copy
NO_CONTENT = 204  # Request succeeded, but no content to send back
RESET_CONTENT = 205  # Instructs the client to reset the document view
PARTIAL_CONTENT = 206  # Partial range requests successful

# Redirection Messages (300–399)
MULTIPLE_CHOICES = 300  # Multiple options for the resource from which the client may choose
MOVED_PERMANENTLY = 301  # This and all future requests should be directed to the given URI
FOUND = 302  # Tells the client to look at (browse to) another URL
SEE_OTHER = 303  # Can be found under a different URL
NOT_MODIFIED = 304  # Indicates that the resource has not been modified since the version specified
TEMPORARY_REDIRECT = 307  # Temporary redirection to a different URL
PERMANENT_REDIRECT = 308  # Permanent redirection to a different URL

# Client Error Responses (400–499)
BAD_REQUEST = 400  # The server cannot process the request due to client error (e.g., malformed request)
UNAUTHORIZED = 401  # Authentication is required and has failed or has not been provided
FORBIDDEN = 403  # The user does not have permission to access the resource
NOT_FOUND = 404  # The requested resource could not be found
METHOD_NOT_ALLOWED = 405  # Request method is not supported for the resource
NOT_ACCEPTABLE = 406  # The requested resource is capable of generating only content not acceptable
PROXY_AUTHENTICATION_REQUIRED = 407  # Proxy authentication required
REQUEST_TIMEOUT = 408  # The server timed out waiting for the request
CONFLICT = 409  # Request conflicts with current state of the server
GONE = 410  # Resource requested is no longer available
LENGTH_REQUIRED = 411  # The request did not specify the length of its content
PRECONDITION_FAILED = 412  # The server does not meet one of the preconditions
PAYLOAD_TOO_LARGE = 413  # Request is larger than the server is willing or able to process
URI_TOO_LONG = 414  # URI provided was too long for the server to process
UNSUPPORTED_MEDIA_TYPE = 415  # Server does not support the media type of the request
RANGE_NOT_SATISFIABLE = 416  # Range specified by the Range header field cannot be fulfilled
EXPECTATION_FAILED = 417  # The server cannot meet the requirements of the Expect request
I_AM_A_TEAPOT = 418  # Joke response, part of the "Hyper Text Coffee Pot Control Protocol" (April Fools' joke)
MISDIRECTED_REQUEST = 421  # Request was directed at a server that is not able to produce a response
UNPROCESSABLE_ENTITY = 422  # WebDAV: Request well-formed but was unable to be followed due to semantic errors
LOCKED = 423  # WebDAV: The resource that is being accessed is locked
FAILED_DEPENDENCY = 424  # WebDAV: The method could not be performed on the resource due to a failed dependency
UPGRADE_REQUIRED = 426  # The client should switch to a different protocol
TOO_MANY_REQUESTS = 429  # The user has sent too many requests in a given amount of time

# Server Error Responses (500–599)
INTERNAL_SERVER_ERROR = 500  # Generic server error
NOT_IMPLEMENTED = 501  # Server does not recognize the request method
BAD_GATEWAY = 502  # Server was acting as a gateway and got an invalid response
SERVICE_UNAVAILABLE = 503  # Server is currently unable to handle the request
GATEWAY_TIMEOUT = 504  # Server was acting as a gateway and did not receive a response
HTTP_VERSION_NOT_SUPPORTED = 505  # Server does not support the HTTP protocol version used in the request
VARIANT_ALSO_NEGOTIATES = 506  # Transparent content negotiation for the request results in a circular reference
INSUFFICIENT_STORAGE = 507  # WebDAV: The server is unable to store the representation needed to complete the request
LOOP_DETECTED = 508  # WebDAV: The server detected an infinite loop while processing the request
NOT_EXTENDED = 510  # Further extensions to the request are required for the server to fulfill it
NETWORK_AUTHENTICATION_REQUIRED = 511  # The client needs to authenticate to gain network access
