import React from 'react';
import styles from './Goals.module.css';
import Image, { StaticImageData } from 'next/image';

interface GoalsProps {
    icon: React.ElementType | StaticImageData; 
    title: string;
    description?: string;
    variant?: 'primary' | 'secondary' | 'tertiary';
}

const Goals: React.FC<GoalsProps> = ({
    icon,
    title,
    description,
    variant = 'primary'
}) => {
    const classNames = `${styles.card} ${styles[variant]}`;

    return (
        <div className={classNames}>
            <div className={styles.icon}>
                {typeof icon === 'function' ? (
                    React.createElement(icon)
                ) : (
                    <Image src={icon} alt={title} width={45} height={45} />
                )}
            </div>
            <h3 className={styles.title} dangerouslySetInnerHTML={{ __html: title }} />
            {description && (
                <p className={styles.description} dangerouslySetInnerHTML={{ __html: description }} />
            )}
        </div>
    );
};

export default Goals;
