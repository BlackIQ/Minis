<!DOCTYPE html>
<html>
<head>
    <meta charset="utf-8">
    <title>Bar Aks</title>
    <link rel="stylesheet" href="bootstrap.css" />
    <style>
        body {
            text-align: center;
            margin-top: 100px;
            background-color: #f1f1f1;
        }
        form {
            margin: auto;
            width: 500px;
            height: 250px;
        }
        i {
            font-size: 25px;
        }
    </style>
</head>
<body>
<form method="post" id="user_form" action="action.php">
    <div class="modal-content">
        <div class="modal-header">
            <h4 class="modal-title">Bar Aks</h4>
        </div>
        <div class="modal-body">
            <h3 class="text-primary">Enter Text</h3>
            <input type="text" class="form-control" name="text">
            <br>
            <?php

            $data = $_POST['text'];
            $len = strlen($data);
            $x = 0;

            while ( $len ) echo '<i class="text-info">' . $data[ --$len ] . '</i>';

            ?>
        </div>
        <div class="modal-footer">
            <button class="btn btn-success" type="submit">Let's Go !</button>
            <button class="btn btn-danger" type="reset">Restart</button>
        </div>
    </div>
</form>
</body>
</html>
