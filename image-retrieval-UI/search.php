<?php

global $saved_filename;
$saved_filename='aa';
function receiveFile(){
    $file=$_FILES['file'];
//    $file_size=$file['size'];
//    if($file_size>2*1024*1024) {
//        echo "文件过大，不能上传大于2M的文件";
//        exit();
//    }

    $file_type=$file['type'];
    if($file_type!="image/jpeg" && $file_type!='image/pjpeg') {
        echo "文件类型只能为jpg格式";
        exit();
    }

    //判断是否上传成功（是否使用post方式上传）
    if(is_uploaded_file($file['tmp_name'])) {
        //把文件转存到目录（不要使用copy函数）
        $uploaded_file=$_FILES['file']['tmp_name'];

        $save_path='/htdocs/image-retrieval-UI/query_images';
        if(!file_exists($save_path))mkdir($save_path);
        $file_true_name=$file['name'];
        global $saved_filename;
        $saved_filename=time().rand(1,1000).substr($file_true_name,strrpos($file_true_name,"."));
        $move_to_file=$save_path."/".$saved_filename;
        //echo "$uploaded_file   $move_to_file";
        if(move_uploaded_file($uploaded_file,iconv("utf-8","gb2312",$move_to_file))) {
            echo $file['name']."上传成功";
        } else {
            echo "上传失败";
        }
    } else {
        echo "上传失败";
    }
}

function requestBySocket(){
    error_reporting(E_ALL);

    $address = '127.0.0.1';
    $port = 15809;

    /* Create a TCP/IP socket. */
    $socket = socket_create(AF_INET, SOCK_STREAM, SOL_TCP);
    if ($socket === false) {
        echo "socket_create() failed: reason: " . socket_strerror(socket_last_error()) . "\n";
    } else {
        echo "OK.\n";
    }

    echo "Attempting to connect to '$address' on port '$port'...";
    $result = socket_connect($socket, $address, $port);
    if ($result === false) {
        echo "socket_connect() failed.\nReason: ($result) " . socket_strerror(socket_last_error($socket)) . "\n";
    } else {
        echo "OK.\n";
    }
    global $saved_filename;
    $request = $saved_filename;
    $response = '';

    socket_write($socket, $request, strlen($request));

    //echo "Reading response
//    $response = socket_read($socket, 2048)
    while ($response = socket_read($socket, 2048)) {
        echo $response;
    }

    echo $saved_filename;
    socket_close($socket);

    return $response;
}

receiveFile();
requestBySocket();

?>