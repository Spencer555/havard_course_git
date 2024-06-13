load balancer takes user and assing it to one of the available servers

methods
random choice
assings randomly to the servers to assign user to 
but is not the best  since it not utilizing resouces effectively

round robin
this assigns the  first user to server 1, second user to server 2 then it continues tills servers are exausted then starts again
it takes longer than other request and its not that great 

fewest connection
when a user make a request pick the one with the fewest connection this is the best but is expensive

load balancing should be done in a session aware way else user would have to log in everytime it redirects to a new server or visit a new page 


session aware load balancing
sticky sessions 
 when u comeback to the load balancer it would remember what server u were sent to last time and send u there again but this can cause a server to get more load than other 

 sessions in database 
  when u store in dbase it does not matter which server u user


  client side sessions 
    using cookies etc and u can use this to store info but u have to authenticate it to prevent tampering and sending data back and forth can be expensive

benchmarking is used to determine how many servers we would need based on estimate of users


autoscaling is used to say lets start with 2 server but scale up when its a peak time most would let u configure a minimun and max amount of servers removing when not in use and and adding when in user

having multiple servers removes the single point of failure where when u have only one server when u re down u re down but with multiple servers when one is down the load balancer redirects to other servers they know this by sending a ping to all the servers every no of seconds and then the load balancer knows if its working or not known as a heartbeat u can use multiple load balancers to prevent from becoming single point of failure 



scaling databases

database partitioning
spliting up a big dbase into multiple parts e.g the flights app airports table user table etc this is vertical partitioning

horizontal partitioning we take a table storing the same type of data and split it into different datasets so flights table is split into domestic flight table and international flight table like taking the data in one table and spliting it into two so if someone is searching for domestic flights  u just search domestic flights table so it becomes efficient but it becomes expensive to join them back


database replication

to prevent single source of failure 

types 
single primary replication 
    we have multiple dbase but one of those dbase is considered to be the primary (where u perform crud on the rest is just read)
    and it also have a single point of failure for write operations

multi primary replication
    we have multiple dbase we can read and write too but when any dbase changes it must inform the other and we might run into uniqueness conflict when two people try to create with same id at the same time and deletion conflict when one trys to delete a row and another tries to update that row
    so we would not like to talk to talk to the dbase if we dont need it



caching - storing a saved version of some info so we can get it quickly and dont need to make a request to a dbase

client side caching - browser stores data so it does not need to rerequest the same info the nxt tym it visits 

to do this we can add this to the header of a http response Cache-Control: max-age=86400
the no of seconds u should cache this resource for

ETag: "747765E74796569676874"
in addition to we can add a etag which is a sequence of characters that identify a particular version of a resource css file, js file etc so it just tells the browser if the etag is the same dont request for a new one

django cache framework
django comes with its own caching framework 

per-view caching  - caching for a view
template fragment Caching  - caching a part of ur template like ur sidebar, footer  etc
low-level Cache api - make an expensive dbase query and save results in cache to access it nxt tym



security  
git 
dont put passwords or any important data or credentials in git if credentials are exposed in repo wipe out all those previous commit because they can be still retrived when someone goes through ur history

html 
phishing  tells u to click on a link and its takes u somewhere else instead of where it the anchor tag says it should take u to 
anyone can copy ur html and pretend to be u 

django 
http and https
info exchange between client and server should be secure encrypted so someone who intercepts it cant decipher it 

secret-key cryptography
u have a plain text and key used in order to encrypt or decrypt info this is used as a cypher text and send and the receiver use the cypher text and key to decrypt it 


public-key cryptography
u have a public key and a private key u share the public key and keep the private key  private so the plaintext is sent with the public key and generate a cypher text and this is sent to the other person which is decrypted with the persons private key so the public key encrypts the private key decrypts 


sql
user passwords should be stored in hashes or hashed version 

e.g forgot password when using this dont tell if there is not email user with this name just tell them email sent

even how long it takes to get info can leak info 

sqlinjection buth with django we are safe from that

apis
rate limiting - no user is able to make more than a certain no of request to api in a certain amount of time this is response to denial of service attack where they make soo many requests that u overwhelm the server or dbase

route authentication - not every one can access any route and need a key to make a api request and dont store ur api keys in ur source codes use envronment variables

javascript
cross site scripting

cross site request forgery 
django is defends this by default with csrf token always use post requests for manipulating something in the dbase