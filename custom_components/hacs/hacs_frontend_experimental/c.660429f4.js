import{_ as e,j as t,e as a,y as i,O as d,d as l,n as s}from"./main-e6d3fb5e.js";import"./c.6795ddb8.js";import"./c.88818c27.js";import"./c.7a38bd55.js";import"./c.8e28b461.js";import"./c.11013a9d.js";import"./c.54b4c8e8.js";let o=e([s("ha-selector-boolean")],(function(e,t){return{F:class extends t{constructor(...t){super(...t),e(this)}},d:[{kind:"field",decorators:[a()],key:"hass",value:void 0},{kind:"field",decorators:[a()],key:"value",value:void 0},{kind:"field",decorators:[a()],key:"label",value:void 0},{kind:"field",decorators:[a()],key:"helper",value:void 0},{kind:"field",decorators:[a({type:Boolean})],key:"disabled",value:()=>!1},{kind:"method",key:"render",value:function(){return i`
      <ha-formfield alignEnd spaceBetween .label=${this.label}>
        <ha-switch
          .checked=${this.value}
          @change=${this._handleChange}
          .disabled=${this.disabled}
        ></ha-switch>
      </ha-formfield>
      ${this.helper?i`<ha-input-helper-text>${this.helper}</ha-input-helper-text>`:""}
    `}},{kind:"method",key:"_handleChange",value:function(e){const t=e.target.checked;this.value!==t&&d(this,"value-changed",{value:t})}},{kind:"get",static:!0,key:"styles",value:function(){return l`
      ha-formfield {
        display: flex;
        height: 56px;
        align-items: center;
        --mdc-typography-body2-font-size: 1em;
      }
    `}}]}}),t);export{o as HaBooleanSelector};
