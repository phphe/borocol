const fs = require('fs')
const viewsPath = '/home/he/www/works/borocol/src/views'
const createCourseViewsPath = viewsPath + '/CreateCourse'
// arr = [1,2,3,4,5,6,7,8,'9a','9b','Tips']
// tpl = '/home/he/www/works/borocol/src/views/CreateCourse0.vue'
// tplStr = fs.readFileSync(tpl).toString()
// arr.forEach(v => {
//   fs.writeFileSync(tpl.replace('0', v), tplStr.replace(/0/g, v))
// })

// arr.unshift(0)
// str = ''
// arr.forEach(v => {
//   str += `{ path: '/CreateCourse${v}', name: 'createCourse${v}', component: resolve => require(['../views/CreateCourse${v}.vue'], resolve), meta: {title: 'Create Course ${v}'}},\n`
// })
// console.log(str);

// str = ''
// arr.forEach(v => {
//   str += `
// div
//   router-link(:to="{name: 'createCourse${v}'}") Create Course ${v}
// `.trim() + '\n'
// })
// console.log(str);

// rename
// const dir = viewsPath + '/' + 'CreateCourse'
// fs.readdirSync(dir).forEach(v => {
//   if (v.match(/\d.vue/)) {
//     const newName = v.replace('CreateCourse', '')
//     fs.renameSync(dir + '/' + v, dir + '/' + newName)
//   }
// })
// fs.watch('./src', { encoding: 'buffer' }, (eventType, filename) => {
//   console.log(eventType);
//   console.log(filename);
// });
// a = `created() {
//     this.$validate(this.validation, this.fields)
//   },
// `;
// [3,4,5,6,7,8,9].forEach(v => {
//   const p =  `${viewsPath}/CreateCourse/Step${v}.vue`
//   let str = fs.readFileSync(p).toString()
//   str = str.replace(/\n\n\n/, '\n')
//   fs.writeFileSync(p, str)
// })
fs.readdirSync(createCourseViewsPath).forEach(v => {
  fs.renameSync(createCourseViewsPath + '/' + v, createCourseViewsPath + '/' + v.replace('Step', 'Page'))
})
