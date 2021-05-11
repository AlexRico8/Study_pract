% rebase('layout.tpl', title='Home Page')


 <img src= "static\image\banner.png">


<div class="row">
    <div class="col-md-4">
        <h2>Porgs</h2>
        <img src= "static\image\porgi.jpg">
        <p>They're from Ahch-To. Luke called them porgs. They're adorable.</p>
        <p><a class="btn btn-default" href=/Porgs>Learn more &raquo;</a></p>
    </div>
    <div class="col-md-4">
        <h2>Ewoks</h2>
        <img src= "static\image\ewoks.jpg">
        <p>The Ewoks are fierce warriors. The top of the food chain on a savage planet!</p>
        <p><a class="btn btn-default" href=/Ewoks>Learn more &raquo;</a></p>
    </div>
    <div class="col-md-4">
        <h2>Wookiee</h2>
        <img src= "static\image\Wookiee.png">
        <p>It's not wise to upset a Wookiee.</p>
        <p><a class="btn btn-default" href=/Wookiee>Learn more &raquo;</a></p>
<h3> Ask a Question </h3>
<form action="/index" method="post">
        <p><textarea rows="2" cols="50" name="QUEST" placeholder="Your question"></textarea></p> 
        <p><input type="text" size="50" name="ADRESS" placeholder="Your email"></p>
        <class="btn btn-default"><input type="submit" value="Send">
</form>
</div>
