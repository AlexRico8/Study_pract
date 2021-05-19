% rebase('layout.tpl', title='Home Page')
<div class="jumbotron">
 <head>
 <h1 align = center>{{title_main}}</h1>
 <body>
 <form action = select1.php method=post>
 <p></p>
  <p align=center>{{title_size}}</p>
  <style>
   select{
   width: 150px;
   }
  </style>
 <p align=center><select name = size[]>
  <option value = 4> 4 </option>
  <option value = 5> 5 </option>
  <option value = 6> 6 </option>
  <option value = 7> 7 </option>
  <option value = 8> 8 </option>
  <option value = 9> 9 </option>
  </select></p>
          <style>
        .button {
        border-radius: 12px;
        background: wight;
        border-color: #cccccc;
        color: white;
        padding: 15px 45px;
        text-align: center;
        text-decoration: none;
        display: inline-block;
        font-size: 16px;
        position: relative;
        left: 50%;
        transform: translate(-50%,0);
        margin: 5% auto;
        cursor: pointer;

        }
        .button1{background-color: #4CAF50;}

        </style>
        <button class="button button1">{{title_enter}}</button>
 </form>
 </body>
 </head>
</div>
<div class="row">
    <p>{{text_main}}</p>
    <div class="col-md-4">
        <h1>{{title2}}</h1>
        <p>{{text2}}</p>
        <p><a class="btn btn-default" href=/Dextra>{{btn_text}}</a></p>
    </div>
    <div class="col-md-4">
        <h1>{{title1}}</h1>
        <p>{{text1}}</p>
        <p><a class="btn btn-default" href=/Prima>{{btn_text}}</a></p>
    </div>
    <div class="col-md-4">
        <h1>{{title3}}</h1>
        <p>{{text3}}</p>
        <p><a class="btn btn-default" href=/Floid>{{btn_text}}</a></p>

</div>


