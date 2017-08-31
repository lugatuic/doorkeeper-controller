<?php

    function verifyUser()
    {
        $uin = $_POST['UIN'];
        $servername = "localhost";
        $username = "";
        $password = "";
        $dbname = "";

        // Create connection
        $conn = new mysqli($servername, $username, $password, $dbname);
        // Check connection
        if ($conn->connect_error) {
            die("Connection failed: " . $conn->connect_error);
        } 
        
        //connect to user end point
        $ch = curl_init("https://acm.cs.uic.edu/rest/api/user/" . $uin);
        curl_setopt($ch, CURLOPT_RETURNTRANSFER, 1);

        //get netid
        $result = curl_exec($ch);
        $json = json_decode($result, true);
        $netid = $json['netid'];

        //connect to other user endpoint
        $ch = curl_init("localhost:5000/username/" . $netid);
        curl_setopt($ch, CURLOPT_RETURNTRANSFER, 1);
        $result = curl_exec($ch);
        $json = json_decode($result, true);
        //compare netid found
        if (isset($json["users"][0])){
            if (strcasecmp($netid, $json["users"][0]["username"])==0)
                $result = 1;
        }
        curl_close($ch);

        //insert/log attempt to database
        $sql = "INSERT INTO swipe_attempts (uin, netid) VALUES ($uin, '$netid')";
        $conn->query($sql);

        // if the user is allowed in.
        if($result == 1){
            return 1;
        }
        return 0;
}

echo verifyUser();
?>
