% rebase('layout.tpl', title='Home Page')


<div>
        <h1>Calculator</h1>
        <p>{{title1}}</p>
        <p>{{title2}}</p>
        
        <style>
        .h4 {
        border-radius: 12px;
        background: white;
        border-color: #cccccc;
        color: black;
        font-size: 9pt;
        height: 70px;
        width: 120px;
        position: fixed;
        right: 950px;
        top: 250px;
        }
        </style>
        <p><a href=/Main><input type=button class=h4  value={{btn_text}}></a></p>
</div>
