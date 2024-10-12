"use client";

import React, { useEffect, useState } from 'react';
import styles from './HeaderMain.module.css';
import Button from '@/app/atoms/Button/Button';

export default function Header() {
  const [isScrolled, setIsScrolled] = useState(false);

  useEffect(() => {
    const handleScroll = () => {
      if (window.scrollY > 25) {
        setIsScrolled(true);
      } else {
        setIsScrolled(false);
      }
    };

    window.addEventListener('scroll', handleScroll);
    
    return () => {
      window.removeEventListener('scroll', handleScroll);
    };
  }, []);

  const handleClick = () => {
    alert('Button Clicked!');
  };

  return (
    <div className={`${styles.container} ${isScrolled ? styles.scrolled : ''}`}>
      <div className={styles.container_items}>
        <h1>LogiConnect</h1>
        <div className={styles.authVariant}>
          <h2>Я вже знайомий</h2>
          <Button
            label="Почати"
            onClick={handleClick}
            variant='primary'
            size='medium'
          />
        </div>
      </div>
    </div>
  );
}
