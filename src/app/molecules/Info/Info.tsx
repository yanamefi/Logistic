"use client";

import React from 'react'
import styles from './Info.module.css'

export default function Info() {
     const handleAboutClick = () => {
        console.log('Про Нас');
      };
    
      const handleSupportClick = () => {
        console.log('Підтримка');
      };
    return (
        <nav className={styles.container} aria-label="Main navigation">
          <div className={styles.information} role="navigation" aria-label="Information links">
            <button onClick={handleAboutClick} aria-label="Про Нас">Про Нас</button>
            <button onClick={handleSupportClick} aria-label="Підтримка">Підтримка</button>
          </div>
          <div className={styles.language} role="navigation" aria-label="Language selection">
            <h3>UA | EN</h3>
          </div>
        </nav>
      );
    };