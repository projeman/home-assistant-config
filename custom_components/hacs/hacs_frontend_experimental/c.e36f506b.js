import{_ as e,j as t,e as a,y as i,O as d,d as o,n as s}from"./main-e6d3fb5e.js";import"./c.5bcc4ef4.js";import"./c.6795ddb8.js";import"./c.7a38bd55.js";import"./c.8e28b461.js";import"./c.11013a9d.js";import"./c.54b4c8e8.js";let l=e([s("ha-selector-template")],(function(e,t){return{F:class extends t{constructor(...t){super(...t),e(this)}},d:[{kind:"field",decorators:[a()],key:"hass",value:void 0},{kind:"field",decorators:[a()],key:"value",value:void 0},{kind:"field",decorators:[a()],key:"label",value:void 0},{kind:"field",decorators:[a()],key:"helper",value:void 0},{kind:"field",decorators:[a({type:Boolean})],key:"disabled",value:()=>!1},{kind:"field",decorators:[a({type:Boolean})],key:"required",value:()=>!0},{kind:"method",key:"render",value:function(){return i`
      ${this.label?i`<p>${this.label}${this.required?" *":""}</p>`:""}
      <ha-code-editor
        mode="jinja2"
        .hass=${this.hass}
        .value=${this.value}
        .readOnly=${this.disabled}
        autofocus
        autocomplete-entities
        autocomplete-icons
        @value-changed=${this._handleChange}
        dir="ltr"
      ></ha-code-editor>
      ${this.helper?i`<ha-input-helper-text>${this.helper}</ha-input-helper-text>`:""}
    `}},{kind:"method",key:"_handleChange",value:function(e){const t=e.target.value;this.value!==t&&d(this,"value-changed",{value:t})}},{kind:"get",static:!0,key:"styles",value:function(){return o`
      p {
        margin-top: 0;
      }
    `}}]}}),t);export{l as HaTemplateSelector};
