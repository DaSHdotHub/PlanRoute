const { defineConfig } = require('@vue/cli-service')
const repoName = process.env.VUE_APP_REPO_NAME;
module.exports = defineConfig({
  transpileDependencies: true,
  publicPath: process.env.NODE_ENV === 'production' ? repoName : '/'
})
