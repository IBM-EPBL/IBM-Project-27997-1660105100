<html lang="en">

<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>MEDIHELP</title>
</head>
<style>
    body {
        background-image: linear-gradient(135deg, #9796f0 10%, #FBC7D4 100%);
        color: darkblue;
    }

    .container1 {
        height: 50px;
        width: 1449px;
        background-image: linear-gradient(135deg, #9796f0 10%, #FBC7D4 100%);
    }

    h1 {
        margin-top: 10px;
        margin-left: 20px;
        margin-right: 23px;
    }

    .container2:hover {
        background-color: yellowgreen;
    }

    a {
        text-decoration: ;
        color: #0f0e0e;
    }

    a:hover {
        color: bluewhite;
    }

    button:hover {
        background-color: white;
        border-color: cadetblue;
    }
</style>

<body>
    <center>
        <h1 style="padding-top:50px">MEDICARE</h1>
        <img src="https://www.commonwealthcarealliance.org/wp-content/uploads/2021/09/Medicare-Definitions-You-Should-Know-scaled.jpg"
            style="height: 80px;width: 80px">
        <br>
        <br>
        <div class="container1">
            <div class="container2" style="float: left">
                <button style="height:50px;">
                    <a href="https://www.medicare.gov/account/login">
                        <H1>Login</H1>
                    </a>
                </button>
            </div>
            <div class="container2" style="float: left">
                <button style="height:50px;">
                    <a href="https://www.medicare.gov/account/login ">
                        <H1>Insurance</H1>
                    </a>
                </button>
            </div>
            <div class="container2" style="float: left">
                <button style="height:50px;">
                    <a href="https://www.medicare.gov/plan-compare">
                        <H1>Find Plans Now</H1>
                    </a>
                </button>
            </div>
            <div class="container2" style="float: left">
                <button style="height:50px;">
                    <a href="https://www.medicare.gov/care-compare">
                        <H1>Find Providers Near Me</H1>
                    </a>
                </button>
            </div>
            <div class="container2" style="float: left">
                <button style="height:50px;">
                    <a href="https://www.medicare.gov/talk-to-someone">
                        <H1>Get Help</H1>
                    </a>

                </button>
            </div>
            <div class="container2" style="float: left">
                <button style="height:50px;">
                    <a href="https://www.medicare.gov/sitemap">
                        <H1>Site Map</H1>
                    </a>

                </button>
            </div>

        </div>
        <br>
        <br>

        <img src="https://image.shutterstock.com/image-vector/medicare-vector-illustration-concept-banner-260nw-1442732906.jpg"
            alt="medicare" style="height:300px">
    </center>

</body>

</html>


<script>
    window.watsonAssistantChatOptions = {
        integrationID: "d63547f8-f695-4dc1-9d49-1427ee71a40c",
        region: "au-syd", // The region your integration is hosted in.
        serviceInstanceID: "37373119-945f-46a0-928a-ced41dc40f36",
        onLoad: function (instance) { instance.render(); }
    };
    setTimeout(function () {
        const t = document.createElement('script');
        t.src = "https://web-chat.global.assistant.watson.appdomain.cloud/versions/" + (window.watsonAssistantChatOptions.clientVersion || 'latest') + "/WatsonAssistantChatEntry.js";
        document.head.appendChild(t);
    });
</script>
