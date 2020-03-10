import React, { useState } from 'react'
import {
  Grid,
  styled,
  TextField,
  InputAdornment,
  Button,
  Typography,
  FormControl,
  InputLabel,
  OutlinedInput
} from '@material-ui/core'

const StyledGrid = styled(Grid)({
  textAlign: 'center'
})

const ListGrid = styled(StyledGrid)({
  background: '#aaaaaa',
  '&:hover': {
    background: '#ed1212'
  }
})

const Paragraph = styled(Typography)({
  'white-space': 'pre-wrap'
})

export default function Index () {
  const [inputText, setInputText] = useState('')
  const [outputText, setOutputText] = useState('')

  const setServerInput = async (text) => {
    const response = await api.post('/api/input', {
      Input: text
    })
    const responseText = await response.data.response
    setOutputText(responseText)
    console.log(responseText)
  }

  const onTextFieldChange = async (e) => {
    e.preventDefault()
    setServerInput(e.target.value)
    setInputText(e.target.value)
  }

  return (
    <>
      <Grid container>
        <StyledGrid item xs={12} lg={6}>
          <FormControl fullWidth variant='outlined'>
            <InputLabel htmlFor='outlined-adornment-amount'>Input field</InputLabel>
            <OutlinedInput
              multiline
              id='outlined-adornment-amount'
              onChange={onTextFieldChange}
              startAdornment={<InputAdornment position='start'>❯</InputAdornment>}
              labelWidth={60}
            />
          </FormControl>
        </StyledGrid>
        <Grid container xs={12} lg={6}>
          <ListGrid item xs={6} lg={3}>
            <Paragraph>
              <h1>Input</h1>
              {inputText}
            </Paragraph>
          </ListGrid>
          <ListGrid item xs={6} lg={3}>
            <Paragraph>
              <h1>Output</h1>
              {outputText}
            </Paragraph>
          </ListGrid>
        </Grid>
      </Grid>
    </>
  )
}
