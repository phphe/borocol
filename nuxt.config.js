const dotenv = require('dotenv')

module.exports = {
  env: require('dotenv').config().parsed,
  /*
  ** Headers of the page
  */
  head: {
    title: 'borocol',
    meta: [
      { charset: 'utf-8' },
      { 'http-equiv': 'X-UA-Compatible', content: 'IE=edge' },
      { name: 'viewport', content: 'width=device-width, initial-scale=1' },
      { hid: 'description', name: 'description', content: 'Nuxt.js project' },
    ],
    link: [
      // { rel: 'icon', type: 'image/x-icon', href: '/favicon.ico' }
      { rel: 'stylesheet', href: 'https://fonts.googleapis.com/css?family=Montserrat:300,400,500,600' },
      { rel: 'stylesheet', href: 'http://at.alicdn.com/t/font_612834_ywypq6ckgi6647vi.css' },
    ],
    script: [
    ],
  },
  /*
  ** Customize the progress bar color
  */
  loading: { color: '#48ccce' },/*
  ** Global CSS
  */
  css: [
    'css-spacing/css/css-spacing.css',
  ],
  //
  babel:{
    "plugins": [["component", [
      {
        "libraryName": "element-ui",
        "styleLibraryName": "theme-default"
      },
      'transform-async-to-generator',
      'transform-runtime'
    ]]],
    comments: true
  },
  /*
  **
  */
  plugins: [
    '@/plugins/axios',
    '@/plugins/element-ui/element-ui',
    {src: '@/plugins/attach-screen-size-to-body', ssr: false},
    '@/plugins/global-components',
    '@/plugins/main',
    {src: '@/plugins/main-server', ssr: true},
    {src: '@/plugins/main-client', ssr: false},
    {src: '@/plugins/vue-data-validator', ssr: false},
  ],
  /*
  ** Build configuration
  */
  build: {
    /*
    ** Run ESLint on save
    */
    extend (config, { isDev, isClient }) {
      if (isDev && isClient) {
        config.module.rules.push({
          enforce: 'pre',
          test: /\.(js|vue)$/,
          loader: 'eslint-loader',
          exclude: /(node_modules)/
        })
      }
    }
  }
}