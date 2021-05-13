let ckey= pm.environment.get('consumerKey');
let csec= pm.environment.get('consumerSecret');
let enc_basic = btoa(ckey +":"+csec);
pm.sendRequest({
    url: `https://${pm.environment.get('host')}/oauth/cc/token`,
    method: 'POST',
    header:{
        'Content-type': 'application/x-www-form-urlencoded',
        'x-api-key': pm.environment.get('consumerKey'),
        'Authorization': `Basic `+ enc_basic,
    },
    body:{
        mode:'raw',
        raw:
            'grant_type=client_credentials'
        }
}, function(err,res){
    let token = res.json().access_token;
    let dni = pm.environment.get("doc_number");
    let hash_id = CryptoJS.SHA256(dni+token).toString();
    pm.environment.set("access_token",token);
    pm.environment.set("hash_id",hash_id);
});
