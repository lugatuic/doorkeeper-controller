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

        $sql = "SELECT uin, status FROM user WHERE uin=$uin AND status=1";
        $result = $conn->query($sql);

        if($result->num_rows >=1){
            return 1;
        }
        return 0;
}

echo verifyUser();
?>
