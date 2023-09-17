import { Box, Button, Flex, Input, Text } from '@chakra-ui/react'
import React from 'react'
import { GoBell } from "react-icons/go";
import logo from '../assets/logo.png'

function Header() {
    return (
        <Box h={'8vh'} borderBottom={'1px'} borderColor={'#cfd5e3'} >
            <Flex alignItems={'center'} justifyContent={'space-between'}>
                <Flex alignItems={'center'}>
                    <Flex flexDir={'row'} alignItems={'center'}>
                        <Box><img src={logo} width={50} /></Box>
                        <Box><Text fontSize={25} fontWeight={400}>Clinic Care</Text></Box>
                    </Flex>
                    <Box ml={10}>
                        <Input size={'sm'} placeholder='Search' variant='outline' />
                    </Box>
                </Flex>


                <Box mr={5}>
                    <Button colorScheme={'blue'} size={'sm'} variant={'outline'}><GoBell /></Button>
                </Box>
            </Flex>
        </Box>
    )
}

export default Header