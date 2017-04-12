<?php

if (isset($_POST['text'])) {
    $ch = curl_init();

    $data = json_encode(['text' => $_POST['text']]);

    curl_setopt($ch, CURLOPT_URL,"http://receiver/post");
    curl_setopt($ch, CURLOPT_CUSTOMREQUEST, "POST");  
    curl_setopt($ch, CURLOPT_POSTFIELDS, $data);
    curl_setopt($ch, CURLOPT_HTTPHEADER, array(                                                                          
        'Content-Type: application/json',                                                                                
        'Content-Length: ' . strlen($data))                                                                       
    );  

    // receive server response ...
    curl_setopt($ch, CURLOPT_RETURNTRANSFER, true);

    $server_output = curl_exec ($ch);

    if ($server_output === FALSE) {
        var_dump(curl_error($ch));
        var_dump(curl_errno($ch));
    }

    curl_close ($ch);

    echo $server_output;

    die;
}

$data = file_get_contents('http://receiver/ranking');
$data = json_decode($data);

$alfa = file_get_contents('http://receiver/letters');
$alfa = json_decode($alfa);

?>
<!DOCTYPE html>
<html lang="en">
  <head>
    <meta charset="utf-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <title>Word Count</title>

    <!-- Bootstrap -->
    <link href="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.7/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-BVYiiSIFeK1dGmJRAkycuHAHRg32OmUcww7on3RYdg4Va+PmSTsz/K68vbdEjh4u" crossorigin="anonymous">

    <!-- HTML5 shim and Respond.js for IE8 support of HTML5 elements and media queries -->
    <!-- WARNING: Respond.js doesn't work if you view the page via file:// -->
    <!--[if lt IE 9]>
      <script src="https://oss.maxcdn.com/html5shiv/3.7.3/html5shiv.min.js"></script>
      <script src="https://oss.maxcdn.com/respond/1.4.2/respond.min.js"></script>
    <![endif]-->
  </head>
  <body>
    <div class="container">
        <h1>Word Count</h1>

        <h2>Submit new text</h2>
        <form>
        <div class="form-group">
            <label class="sr-only" for="text">Text: </label>
            <input type="text" class="form-control" id="text" value="one two one two one two tree one one one" placeholder="....">
        </div>
        <button type="button" id="submit" class="btn btn-primary">Submit text</button>
        </form>

        <h2>Statistics<h2>
        <h3>Words<h3>
        <div id="statistics" class="well">
        <?php foreach($data as $row): ?>
            <p><b><?=$row->position; ?></b>: <?=$row->value; ?></p>
        <?php endforeach; ?>
        </div>

        <h3>Letters<h3>
        <div id="statistics_letters" class="row">
            <?php foreach($alfa as $row): ?>
            <div class="col-xs-4">
                <b><?=$row->letter; ?></b>: <?=$row->value; ?>
            </div>
            <?php endforeach; ?>
        </div>
    </div>
    
    <!-- jQuery (necessary for Bootstrap's JavaScript plugins) -->
    <script src="https://ajax.googleapis.com/ajax/libs/jquery/1.12.4/jquery.min.js"></script>
    <!-- Include all compiled plugins (below), or include individual files as needed -->
    <script src="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.7/js/bootstrap.min.js" integrity="sha384-Tc5IQib027qvyjSMfHjOMaLkfuWVxZxUPnCJA7l2mCWNIpG9mGCD8wGNIcPD7Txa" crossorigin="anonymous"></script>

    <script type="text/javascript">
    $(function() {
        $("#submit").click(function(e){
            e.preventDefault();
            $.ajax({
                type: "POST",
                url: '/',
                data: {
                    "text": $("#text").val()
                }
            });
        });
    });
    </script>
  </body>
</html>
