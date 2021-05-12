% rebase('layout.tpl', title='Home Page')


<div>
        <h1>Calculator</h1>
        <p>{{title1}}</p>
        <p>{{title2}}</p>
        
        <style>
        .h4 {
        border-radius: 4px;
        background: white;
        color: black;
        font-size: 9pt;
        height: 70px;
        width: 120px;
        position: fixed;
        right: 950px;
        top: 250px;
        }
        </style>
        <p><input type=button class=h4 onclick=/Main value={{btn_text}}></p>
</div>
