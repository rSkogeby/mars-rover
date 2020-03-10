import axios from 'axios'
import getConfig from 'next/config'

const { publicRuntimeConfig, serverRuntimeConfig } = getConfig()
const api = axios.create({
  baseURL: serverRuntimeConfig.apiHost || publicRuntimeConfig.apiHost
})
console.log('THE ADDRESS: ' + serverRuntimeConfig.apiHost || publicRuntimeConfig.apiHost)

export default api
