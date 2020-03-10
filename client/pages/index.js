import React from 'react'
import {
  Grid,
  styled,
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

export default function Index () {
  return (
    <>
      <Grid container>
        <StyledGrid item xs={12} lg={6}>
          <p> Hello </p>
        </StyledGrid>
        <Grid container xs={12} lg={6}>
          <ListGrid item xs={6} lg={3}>
            <h1>Input</h1>
          </ListGrid>
          <ListGrid item xs={6} lg={3}>
            <h1>Output</h1>
          </ListGrid>
        </Grid>
      </Grid>
    </>
  )
}
