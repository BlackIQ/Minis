<!-- Html By Amir -->
<!DOCTYPE html>
<html>
<head>
    <meta charset="utf-8">
    <title>IP</title>
    <link rel="stylesheet" href="../bootstrap.css" />
    <style>
        body {
            text-align: center;
            margin-top: 100px;
            background-color: #f1f1f1;
        }
        .form {
            margin: auto;
            width: 500px;
            height: 250px;
        }
    </style>
</head>
<body>
<div class="form">
    <div class="modal-content">
        <div class="modal-header">
            <h4 class="modal-title">IP</h4>
        </div>
        <div class="modal-body">
            <?php
                function getUserIpAddress() {
                    if(!empty($_SERVER['HTTP_CLIENT_IP'])) {
                        //ip from share internet
                        $ip = $_SERVER['HTTP_CLIENT_IP'];
                    }
                    elseif(!empty($_SERVER['HTTP_X_FORWARDED_FOR'])) {
                        //ip pass from proxy
                        $ip = $_SERVER['HTTP_X_FORWARDED_FOR'];
                    }
                    else{
                        $ip = $_SERVER['REMOTE_ADDR'];
                    }
                    return $ip;
                }

                echo '<h3 class="text-info">Your IP Is</h3>';
                echo '<h1 class="text-success">' . getUserIpAddress() . '</h1>';
            ?>
        </div>
    </div>
</div>
</body>
</html>
