<%inherit file="banner_editor:templates/layout.mako"/>


<div class="flexslider">
    <ul class="slides">
        %for banner in query:
    <li>
        <a href="${banner.url}"><img src="/static/image/${banner.image}">  </a>
    </li>
        %endfor
    </ul>
</div>


