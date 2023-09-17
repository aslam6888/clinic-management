import * as React from 'react'

import './App.css'
import { ChakraProvider, Flex, Box } from '@chakra-ui/react'
import SideNav from './components/SideNav';
import Header from './components/Header';
import { Route, Routes } from 'react-router-dom';
import Dashbaord from './pages/Dashboard';
import Doctors from './pages/Doctors';


function App() {
  return (
    <ChakraProvider>
      <AppLayout />
    </ChakraProvider>
  )
}

function AppLayout() {
  return (
    <Flex h={'100vh'} overflow={'hidden'} flexDir={'column'}>
      <Header />
      <Flex>
        <SideNav />
        <Flex w={'100%'} backgroundColor={'#edf1fa'} flexDirection={'column'} overflowY={'scroll'}>
          <Box px={10} py={5}>
            <Routes>
              <Route path={'/'} element={<Dashbaord />} />
              <Route path={'/doctors'} element={<Doctors />} />
            </Routes>
          </Box>

        </Flex>
      </Flex>

    </Flex>
  )
}
export default App;
