import React from 'react'
import styles from './OurGoal.module.css'
import Goals from '@/app/atoms/Goals/Goals'
import Multiple_device from './img/Multiple Devices.png'
import Collaboration from './img/Collaboration.png'
import Protect from './img/Protect.png'

export default function OurGoal() {
  return (
    <div className={styles.container}>
      <h1>Яка наша ціль?</h1>
      <div className={styles.itemsContainer}>  
        <Goals 
            icon={Multiple_device}
            title="Ефективна<br /> платформа"
            description="Створюємо інноваційний<br /> сервіс для організації<br /> вантажоперевезень онлайн."
            />
         <Goals 
            icon={Collaboration}
            title="Легка<br /> взаємодія"
            description="Полегшуємо пошук і співпрацю<br /> між вантажовідправниками та<br /> перевізниками."
            />
         <Goals 
            icon={Protect}
            title="Прозорість і<br /> надійність"
            description="Гарантуємо надійність і<br /> прозорість у всіх логістичних<br /> операціях."
            />
      </div>
    </div>
  )
}
