webpackJsonp([5],{"1jB/":function(e,t,s){"use strict";Object.defineProperty(t,"__esModule",{value:!0});var a={extends:s("7Xc1").a,data:function(){var e=this.$state.createCourse,t=e.fields,s=e.validations,a=e.pageOrder[e.getRouteIndex()];return{name:a,fields:t[a],validation:s[a]}},created:function(){this.$validate(this.validation,this.fields)}},i={render:function(){var e=this,t=e.$createElement,s=e._self._c||t;return s("div",{staticClass:"CreateCourse6"},[s("div",{staticClass:"content-card"},[e._m(0),e._m(1),s("div",{staticClass:"content-card-body has-tips"},[s("form",[s("div",{staticClass:"form-group"},[s("label",[e._v(e._s(e.fields.guestRequirement.required?"* ":"")+e._s(e.fields.guestRequirement.text))]),s("textarea",{directives:[{name:"model",rawName:"v-model",value:e.fields.guestRequirement.value,expression:"fields.guestRequirement.value"}],staticClass:"form-control",attrs:{rows:"3",placeholder:"- Skill level\n- Occupations"},domProps:{value:e.fields.guestRequirement.value},on:{input:function(t){t.target.composing||e.$set(e.fields.guestRequirement,"value",t.target.value)}}})]),s("div",{staticClass:"form-group"},[s("label",[e._v(e._s(e.fields.requestFormExisted.required?"* ":"")+e._s(e.fields.requestFormExisted.text))]),s("CheckboxGroup",{attrs:{multiple:!1},model:{value:e.fields.requestFormExisted.value,callback:function(t){e.$set(e.fields.requestFormExisted,"value",t)},expression:"fields.requestFormExisted.value"}},[s("Checkbox",{staticClass:"mls",attrs:{value:!1}}),s("span",{staticClass:"mls"},[e._v("No")]),s("Checkbox",{staticClass:"mls",attrs:{value:!0}}),s("span",{staticClass:"mls"},[e._v("Yes")])],1)],1),s("div",{staticClass:"_1"},e._l(e.fields.requestForm.value,function(t,a){return s("div",{staticClass:"form-group"},[s("Checkbox",{model:{value:t.enabled,callback:function(s){e.$set(t,"enabled",s)},expression:"item.enabled"}}),s("span",{staticClass:"mls"},[e._v("Question "+e._s(a+1)+" :")]),s("textarea",{directives:[{name:"model",rawName:"v-model",value:t.value,expression:"item.value"}],staticClass:"form-control mls",attrs:{rows:"3"},domProps:{value:t.value},on:{input:function(s){s.target.composing||e.$set(t,"value",s.target.value)}}}),s("div",{staticClass:"clearfix"})],1)}))]),s("Tips")],1)])])},staticRenderFns:[function(){var e=this.$createElement,t=this._self._c||e;return t("div",{staticClass:"content-card-header"},[t("div",{staticClass:"step"},[this._v(" Step 6")]),t("div",{staticClass:"title"})])},function(){var e=this.$createElement,t=this._self._c||e;return t("div",{staticClass:"content-card-progress-bar progress"},[t("div",{staticClass:"progress-bar progress-bar-warning",staticStyle:{width:"66%"},attrs:{role:"progressbar"}},[this._v("66%")])])}]},r=s("8AGX")(a,i,!1,function(e){s("GxGJ")},null,null);t.default=r.exports},GxGJ:function(e,t){}});
//# sourceMappingURL=5.9cdd55570521aaabdff7.js.map