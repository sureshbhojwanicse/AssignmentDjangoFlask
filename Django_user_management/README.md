# Django_user_management

Deployed on : Django rest api<br/>
Sample Data used : User Information Open json dataset

Access:<br/>
Input : JSON Post hit 

## Sample Payloads:<br/>

1. Returns all the data when empty json passed over the network:<br/>
Ex:http://serverip:8000/model/ <br/>
Req type : POST <br/>
Payload data : {}

2. Returns related data when all passed data matched to a record<br/>
Ex:http://serverip:8000/model/<br/>
Req type : POST <br/>
Payload data : {
    "email": "melany.wijngaard@example.com",
    "gender": "female",
    "birthdate": 608022796,
   "username": "bigpeacock217",
    "first_name": "melany",
    "last_name": "wijngaard"}

# Future Improvments:

1. Faster search, indexing, caching can be applied
2. Secutiry by binding IPs
3. Load Balancers can be applied for huge traffic
4. Deeplearning based model can be applied for string based search if there is a text corpus to search
5. Similarity based algorithms can be used
