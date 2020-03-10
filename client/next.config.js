function getConfigVar (name) {
  if (process.env.npm_lifecycle_event === 'prepare') return null
  if (!process.env[name]) throw new Error(`Missing environmental variable: ${name}`)
  console.log('my envr var', process.env[name])
  return process.env[name]
}

module.exports = {
  publicRuntimeConfig: {
    apiHost: getConfigVar('PUBLIC_API_HOST')
  },
  serverRuntimeConfig: {
    apiHost: getConfigVar('INTERNAL_API_HOST')
  }
}
